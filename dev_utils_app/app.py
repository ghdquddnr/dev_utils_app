"""메인 애플리케이션 클래스"""

import os
import sys
import json
import customtkinter as ctk
from PIL import Image

from dev_utils_app.utils.theme import ThemeManager
from dev_utils_app.views.sidebar import Sidebar
from dev_utils_app.views.text_diff import TextDiffView

# 기본 테마 설정
ctk.set_appearance_mode("system")  # 시스템 테마 따라가기
ctk.set_default_color_theme("blue")  # 기본 색상 테마

class App(ctk.CTk):
    """메인 애플리케이션 클래스"""
    
    def __init__(self):
        super().__init__()
        
        # 앱 설정
        self.title("개발 유틸리티 앱")
        
        # 화면 크기 및 위치 설정
        width = 1200
        height = 800
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")
        
        self.minsize(800, 600)
        
        # 테마 관리자
        self.theme_manager = ThemeManager(self)
        
        # 기본 그리드 설정
        self.grid_columnconfigure(1, weight=1)  # 콘텐츠 영역이 확장되도록
        self.grid_rowconfigure(0, weight=1)
        
        # 사이드바 생성
        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        # 뷰 생성 및 기본 뷰 설정
        self.current_view = None
        self.create_views()
        self.show_view("text_diff")
    
    def create_views(self):
        """모든 뷰 생성"""
        self.views = {
            "text_diff": TextDiffView(self)
        }
        
        # 모든 뷰를 그리드에 배치
        for view in self.views.values():
            view.grid(row=0, column=1, sticky="nsew")
            view.grid_remove()  # 초기에는 숨김
    
    def show_view(self, view_name):
        """지정된 뷰 표시"""
        # 현재 표시된 뷰가 있으면 숨김
        if self.current_view:
            self.current_view.grid_remove()
        
        # 새 뷰 표시
        self.views[view_name].grid()
        self.current_view = self.views[view_name]
        
        # 사이드바에서 선택된 항목 업데이트
        self.sidebar.select_item(view_name) 