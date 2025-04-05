"""사이드바 뷰"""

import os
import customtkinter as ctk
from PIL import Image

class Sidebar(ctk.CTkFrame):
    """애플리케이션 사이드바"""
    
    def __init__(self, master):
        super().__init__(master, width=220, corner_radius=0)
        self.master = master
        
        # 사이드바는 너비 고정
        self.grid_propagate(False)
        
        # 로고와 타이틀
        self.logo_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.logo_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(20, 10))
        
        self.logo_label = ctk.CTkLabel(
            self.logo_frame, 
            text="개발자 유틸리티", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=10, pady=10)
        
        # 메뉴 항목 프레임
        self.menu_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.menu_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # 메뉴 버튼 생성
        self.menu_items = {
            "text_diff": {
                "text": "텍스트 비교",
                "command": lambda: self.master.show_view("text_diff"),
                "button": None
            }
        }
        
        # 메뉴 버튼 생성 및 배치
        for i, (key, item) in enumerate(self.menu_items.items()):
            btn = ctk.CTkButton(
                self.menu_frame,
                text=item["text"],
                anchor="w",
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"),
                height=45,
                corner_radius=6,
                font=ctk.CTkFont(size=14),
                command=item["command"]
            )
            btn.grid(row=i, column=0, sticky="ew", padx=5, pady=5)
            self.menu_items[key]["button"] = btn
        
        # 하단 프레임 (설정 등)
        self.bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.bottom_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=20)
        
        # 테마 전환 버튼
        self.theme_button = ctk.CTkButton(
            self.bottom_frame, 
            text="테마 변경", 
            command=self.master.theme_manager.toggle_theme,
            fg_color="transparent",
            border_width=1,
            height=40,
            font=ctk.CTkFont(size=14),
            text_color=("gray10", "gray90")
        )
        self.theme_button.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        
        # 기본 메뉴 선택
        self.selected_menu = None
    
    def select_item(self, item_key):
        """메뉴 항목 선택"""
        # 이전 선택 해제
        if self.selected_menu and self.selected_menu in self.menu_items:
            self.menu_items[self.selected_menu]["button"].configure(
                fg_color="transparent"
            )
        
        # 새 항목 선택
        if item_key in self.menu_items:
            self.menu_items[item_key]["button"].configure(
                fg_color=("gray75", "gray25")
            )
            self.selected_menu = item_key 