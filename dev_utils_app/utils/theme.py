"""테마 관리 유틸리티"""

import os
import json
import customtkinter as ctk

class ThemeManager:
    """앱의 테마를 관리하는 클래스"""
    
    def __init__(self, app):
        self.app = app
        self.current_theme = "system"  # 기본값: 시스템 설정 따라가기
        
        # 설정 파일 경로
        self.config_dir = os.path.join(os.path.expanduser("~"), ".dev_utils_app")
        self.config_file = os.path.join(self.config_dir, "config.json")
        
        # 설정 로드
        self.load_settings()
    
    def load_settings(self):
        """설정 파일 로드"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    config = json.load(f)
                    self.current_theme = config.get("theme", "system")
                    self.apply_theme(self.current_theme)
            except (json.JSONDecodeError, IOError):
                # 파일 로드 실패 시 기본값 사용
                self.apply_theme(self.current_theme)
        else:
            # 설정 파일이 없으면 기본값 사용하고 디렉토리 생성
            os.makedirs(self.config_dir, exist_ok=True)
            self.save_settings()
    
    def save_settings(self):
        """설정 파일 저장"""
        os.makedirs(self.config_dir, exist_ok=True)
        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump({"theme": self.current_theme}, f)
    
    def toggle_theme(self):
        """라이트/다크 모드 전환"""
        if self.current_theme == "dark":
            self.apply_theme("light")
        elif self.current_theme == "light":
            self.apply_theme("dark")
        else:  # system
            # 시스템 설정이면 다크 모드로 전환
            self.apply_theme("dark")
    
    def apply_theme(self, theme):
        """테마 적용"""
        self.current_theme = theme
        ctk.set_appearance_mode(theme)
        self.save_settings() 