"""텍스트 비교 뷰"""

import customtkinter as ctk
from diff_match_patch import diff_match_patch

class TextDiffView(ctk.CTkFrame):
    """텍스트 비교 기능을 제공하는 뷰"""
    
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        # 레이아웃 설정 - 화면 크기에 맞게 조정될 수 있도록 수정
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=0)  # 제목 영역은 고정 크기
        self.grid_rowconfigure(1, weight=10)  # 텍스트 영역은 화면 크기에 따라 확장
        self.grid_rowconfigure(2, weight=0)  # 버튼 영역은 고정 크기
        
        # 제목
        self.title_label = ctk.CTkLabel(
            self, 
            text="텍스트 비교 (Text Diff)", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.grid(row=0, column=0, columnspan=2, sticky="nw", padx=20, pady=(10, 5))
        
        # 텍스트 프레임 (두 텍스트 영역을 포함)
        self.text_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.text_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=20, pady=10)
        self.text_frame.grid_columnconfigure((0, 1), weight=1, uniform="group1")
        self.text_frame.grid_rowconfigure(0, weight=0)  # 라벨
        self.text_frame.grid_rowconfigure(1, weight=1)  # 텍스트 영역
        
        # 원본 텍스트 라벨
        self.source_label = ctk.CTkLabel(
            self.text_frame, 
            text="원본 텍스트", 
            font=ctk.CTkFont(size=16)
        )
        self.source_label.grid(row=0, column=0, sticky="w", padx=10, pady=(0, 5))
        
        # 비교 텍스트 라벨
        self.target_label = ctk.CTkLabel(
            self.text_frame, 
            text="비교 텍스트", 
            font=ctk.CTkFont(size=16)
        )
        self.target_label.grid(row=0, column=1, sticky="w", padx=10, pady=(0, 5))
        
        # 원본 텍스트 에어리어
        self.source_text = ctk.CTkTextbox(
            self.text_frame, 
            wrap="word"
        )
        self.source_text.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        
        # 비교 텍스트 에어리어
        self.target_text = ctk.CTkTextbox(
            self.text_frame, 
            wrap="word"
        )
        self.target_text.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)
        
        # 결과 프레임
        self.result_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.result_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=10)
        self.result_frame.grid_columnconfigure((0, 1), weight=1)
        
        # 버튼 프레임 (중앙 정렬)
        self.button_frame = ctk.CTkFrame(self.result_frame, fg_color="transparent")
        self.button_frame.grid(row=0, column=0, columnspan=2)
        self.button_frame.grid_columnconfigure((0, 1), weight=1)
        
        # 비교 버튼
        self.compare_button = ctk.CTkButton(
            self.button_frame, 
            text="비교하기", 
            font=ctk.CTkFont(size=16),
            command=self.compare_texts,
            width=150,
            height=40
        )
        self.compare_button.grid(row=0, column=0, padx=10, pady=10)
        
        # 초기화 버튼
        self.reset_button = ctk.CTkButton(
            self.button_frame, 
            text="초기화", 
            font=ctk.CTkFont(size=16),
            command=self.clear_all,
            width=150,
            height=40
        )
        self.reset_button.grid(row=0, column=1, padx=10, pady=10)
        
        # 태그 설정
        self.setup_tags()
        
    def setup_tags(self):
        """텍스트 영역에 태그 설정"""
        # 원본 텍스트 에어리어 태그
        self.source_text.tag_config("diff_delete", background="#FFCCCC")
        self.source_text.tag_config("diff_insert", background="#CCFFCC")
        
        # 비교 텍스트 에어리어 태그
        self.target_text.tag_config("diff_delete", background="#FFCCCC")
        self.target_text.tag_config("diff_insert", background="#CCFFCC")
    
    def compare_texts(self):
        """두 텍스트 비교"""
        # 텍스트 가져오기
        source_content = self.source_text.get("1.0", "end-1c")
        target_content = self.target_text.get("1.0", "end-1c")
        
        # 이전 태그 제거
        self.clear_tags()
        
        # 차이점 찾기
        dmp = diff_match_patch()
        diffs = dmp.diff_main(source_content, target_content)
        dmp.diff_cleanupSemantic(diffs)
        
        # 원본 텍스트에 태그 적용
        source_lines = source_content.split('\n')
        target_lines = target_content.split('\n')
        
        # 라인별 비교
        for i, (s_line, t_line) in enumerate(zip(source_lines, target_lines)):
            if s_line != t_line:
                # 현재 줄에 태그 적용
                line_num = i + 1
                self.source_text.tag_add("diff_delete", f"{line_num}.0", f"{line_num}.end")
                self.target_text.tag_add("diff_insert", f"{line_num}.0", f"{line_num}.end")
        
        # 줄 수가 다른 경우 추가/삭제된 줄 처리
        s_len = len(source_lines)
        t_len = len(target_lines)
        
        if s_len > t_len:
            # 원본에 더 많은 줄이 있는 경우
            for i in range(t_len, s_len):
                line_num = i + 1
                self.source_text.tag_add("diff_delete", f"{line_num}.0", f"{line_num}.end")
        elif t_len > s_len:
            # 비교 텍스트에 더 많은 줄이 있는 경우
            for i in range(s_len, t_len):
                line_num = i + 1
                self.target_text.tag_add("diff_insert", f"{line_num}.0", f"{line_num}.end")
    
    def clear_tags(self):
        """모든 태그 제거"""
        self.source_text.tag_remove("diff_delete", "1.0", "end")
        self.source_text.tag_remove("diff_insert", "1.0", "end")
        self.target_text.tag_remove("diff_delete", "1.0", "end")
        self.target_text.tag_remove("diff_insert", "1.0", "end")
    
    def clear_all(self):
        """모든 텍스트와 태그 초기화"""
        # 텍스트 초기화
        self.source_text.delete("1.0", "end")
        self.target_text.delete("1.0", "end")
        
        # 태그 초기화
        self.clear_tags() 