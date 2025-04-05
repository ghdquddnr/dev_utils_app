"""JSON 뷰어 뷰"""

import json
import customtkinter as ctk
from tkinter import ttk
import tkinter as tk

class JsonTreeView(ttk.Treeview):
    """JSON 구조를 표시하는 트리 뷰"""
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # 스타일 설정
        style = ttk.Style()
        style.configure("Treeview", 
                        background="gray95",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="gray95")
        style.map('Treeview', 
                  background=[('selected', '#347083')])
        
        # 다크 모드/라이트 모드 테마 변경 감지
        self.update_theme()
    
    def update_theme(self):
        """현재 테마에 따라 트리뷰 색상 업데이트"""
        mode = ctk.get_appearance_mode()
        style = ttk.Style()
        
        if mode == "Dark":
            style.configure("Treeview", 
                            background="#2b2b2b",
                            foreground="#ffffff",
                            fieldbackground="#2b2b2b")
            style.map('Treeview', 
                      background=[('selected', '#347083')])
        else:
            style.configure("Treeview", 
                            background="gray95",
                            foreground="black",
                            fieldbackground="gray95")
            style.map('Treeview', 
                      background=[('selected', '#347083')])

class JsonViewerView(ctk.CTkFrame):
    """JSON 뷰어 기능을 제공하는 뷰"""
    
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        # 레이아웃 설정 - 화면 크기에 맞게 조정될 수 있도록 수정
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=0)  # 제목 영역은 고정 크기
        self.grid_rowconfigure(1, weight=10)  # 콘텐츠 영역은 화면 크기에 따라 확장
        self.grid_rowconfigure(2, weight=0)  # 버튼 영역은 고정 크기
        
        # 제목
        self.title_label = ctk.CTkLabel(
            self, 
            text="JSON 뷰어", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.grid(row=0, column=0, columnspan=2, sticky="nw", padx=20, pady=(10, 5))
        
        # 콘텐츠 프레임 (왼쪽 JSON 입력, 오른쪽 트리 뷰)
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=20, pady=10)
        self.content_frame.grid_columnconfigure((0, 1), weight=1, uniform="group1")
        self.content_frame.grid_rowconfigure(0, weight=0)  # 라벨
        self.content_frame.grid_rowconfigure(1, weight=1)  # 콘텐츠 영역
        
        # 입력 JSON 라벨
        self.input_label = ctk.CTkLabel(
            self.content_frame, 
            text="JSON 입력", 
            font=ctk.CTkFont(size=16)
        )
        self.input_label.grid(row=0, column=0, sticky="w", padx=10, pady=(0, 5))
        
        # JSON 구조 라벨
        self.output_label = ctk.CTkLabel(
            self.content_frame, 
            text="JSON 구조", 
            font=ctk.CTkFont(size=16)
        )
        self.output_label.grid(row=0, column=1, sticky="w", padx=10, pady=(0, 5))
        
        # 입력 JSON 텍스트 영역
        self.input_text = ctk.CTkTextbox(
            self.content_frame, 
            wrap="word"
        )
        self.input_text.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        
        # JSON 트리 뷰 프레임 (트리뷰를 담는 컨테이너)
        self.tree_container = ctk.CTkFrame(self.content_frame)
        self.tree_container.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)
        self.tree_container.grid_columnconfigure(0, weight=1)
        self.tree_container.grid_rowconfigure(0, weight=1)
        
        # 트리 뷰는 tkinter를 사용 (CustomTkinter에는 없음)
        self.tree = JsonTreeView(
            self.tree_container,
            columns=("value",),
            show="tree"
        )
        self.tree.column("#0", width=200)
        self.tree.column("value", width=200)
        self.tree.heading("#0", text="키")
        self.tree.heading("value", text="값")
        self.tree.grid(row=0, column=0, sticky="nsew")
        
        # 스크롤바 추가
        self.tree_scrollbar = ctk.CTkScrollbar(
            self.tree_container, 
            command=self.tree.yview
        )
        self.tree_scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=self.tree_scrollbar.set)
        
        # 버튼 프레임
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=10)
        self.button_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        # 변환 버튼
        self.convert_button = ctk.CTkButton(
            self.button_frame, 
            text="변환하기", 
            font=ctk.CTkFont(size=16),
            command=self.parse_json,
            width=150,
            height=40
        )
        self.convert_button.grid(row=0, column=0, padx=10, pady=10)
        
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
        
        # 예제 버튼
        self.example_button = ctk.CTkButton(
            self.button_frame, 
            text="예제 데이터", 
            font=ctk.CTkFont(size=16),
            command=self.load_example,
            width=150,
            height=40
        )
        self.example_button.grid(row=0, column=2, padx=10, pady=10)
        
        # 모두 펼치기/접기 버튼
        self.expand_button = ctk.CTkButton(
            self.button_frame, 
            text="모두 펼치기", 
            font=ctk.CTkFont(size=16),
            command=self.toggle_expand,
            width=150,
            height=40
        )
        self.expand_button.grid(row=0, column=3, padx=10, pady=10)
        
        # 상태 변수
        self.is_expanded = False
        
        # 테마 리스너 등록
        self.master.theme_manager.add_theme_listener(self.tree)
    
    def parse_json(self):
        """JSON 파싱 및 트리 뷰에 표시"""
        # 이전 트리 내용 삭제
        self.tree.delete(*self.tree.get_children())
        
        # JSON 텍스트 가져오기
        json_text = self.input_text.get("1.0", "end-1c")
        
        try:
            # JSON 파싱
            json_data = json.loads(json_text)
            # 트리 생성
            self.build_tree("", json_data)
            self.is_expanded = True
            self.expand_button.configure(text="모두 접기")
        except json.JSONDecodeError as e:
            # 에러 발생 시 처리
            self.tree.insert("", "end", text="파싱 에러", values=(str(e),))
    
    def build_tree(self, parent, json_data, key="root"):
        """재귀적으로 JSON 트리 구축"""
        if parent == "":
            node = self.tree.insert(parent, "end", text=key, open=True)
        else:
            node = parent
            
        if isinstance(json_data, dict):
            # 딕셔너리인 경우 키-값 쌍으로 처리
            for k, v in json_data.items():
                if isinstance(v, (dict, list)):
                    child = self.tree.insert(node, "end", text=k, open=True)
                    self.build_tree(child, v, k)
                else:
                    self.tree.insert(node, "end", text=k, values=(str(v),))
        elif isinstance(json_data, list):
            # 리스트인 경우 인덱스-값 쌍으로 처리
            for i, item in enumerate(json_data):
                if isinstance(item, (dict, list)):
                    child = self.tree.insert(node, "end", text=f"[{i}]", open=True)
                    self.build_tree(child, item, f"[{i}]")
                else:
                    self.tree.insert(node, "end", text=f"[{i}]", values=(str(item),))
        else:
            # 기본 타입의 경우 바로 값 표시
            self.tree.insert(node, "end", text=key, values=(str(json_data),))
    
    def clear_all(self):
        """모든 내용 초기화"""
        self.input_text.delete("1.0", "end")
        self.tree.delete(*self.tree.get_children())
        self.is_expanded = False
        self.expand_button.configure(text="모두 펼치기")
    
    def toggle_expand(self):
        """모든 노드 펼치기/접기 토글"""
        nodes = self.get_all_children(self.tree)
        
        if self.is_expanded:
            # 모두 접기
            for node in nodes:
                self.tree.item(node, open=False)
            self.expand_button.configure(text="모두 펼치기")
            self.is_expanded = False
        else:
            # 모두 펼치기
            for node in nodes:
                self.tree.item(node, open=True)
            self.expand_button.configure(text="모두 접기")
            self.is_expanded = True
    
    def get_all_children(self, tree, item=""):
        """트리의 모든 자식 노드 가져오기"""
        children = tree.get_children(item)
        result = list(children)
        
        for child in children:
            result.extend(self.get_all_children(tree, child))
            
        return result
    
    def update_theme(self):
        """테마 변경 시 호출"""
        self.tree.update_theme()
    
    def load_example(self):
        """예제 JSON 데이터 로드"""
        example_json = """{
  "name": "John Doe",
  "age": 30,
  "isEmployed": true,
  "address": {
    "street": "123 Main St",
    "city": "Boston",
    "zipCode": "02101"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212-555-1234"
    },
    {
      "type": "work",
      "number": "646-555-4567"
    }
  ],
  "children": [],
  "spouse": null
}"""
        # 기존 내용 삭제 후 예제 데이터 설정
        self.input_text.delete("1.0", "end")
        self.input_text.insert("1.0", example_json)
        
        # 즉시 변환
        self.parse_json() 