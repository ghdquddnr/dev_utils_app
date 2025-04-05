# 开发者实用工具应用 (Dev Utils App)

一个为开发者提供各种实用功能的Python GUI应用程序。通过现代化的UI和便捷的功能，使开发工作更加高效。

![应用程序截图](screenshot.png)

## 主要功能

### 文本比较 (Text Diff)
- 直观显示两段文本之间的差异
- 通过逐行比较实现精确的差异高亮
- 直观的UI界面，使用简便
- 重置按钮可快速开始新的工作

### JSON查看器
- 将JSON字符串可视化为树形结构
- 节点折叠/展开功能，轻松浏览复杂结构
- 提供示例数据以便快速测试
- 根据亮色/暗色模式自动调整主题

## 技术栈

- **前端**: CustomTkinter (Python GUI库)
- **比较算法**: diff-match-patch库
- **JSON解析**: Python内置json模块
- **主题系统**: 支持亮色/暗色模式

## 系统要求

- Python 3.8或更高版本
- 以下Python包:
  - customtkinter
  - pillow
  - diff-match-patch

## 安装方法

### 1. 克隆仓库
```bash
git clone https://github.com/ghdquddnr/dev_utils_app.git
cd dev_utils_app
```

### 2. 设置虚拟环境并安装包
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 安装包
pip install customtkinter pillow diff-match-patch
```

### 3. 运行应用程序
```bash
python main.py
```

## 使用方法

### 文本比较功能
1. 在左侧文本区域输入原始文本。
2. 在右侧文本区域输入要比较的文本。
3. 点击"比较"按钮，两段文本之间的差异将以颜色显示。
   - 删除的部分: 红色背景
   - 添加的部分: 绿色背景
4. 点击"重置"按钮可清除所有文本并开始新的比较。

### JSON查看器功能
1. 在左侧文本区域输入JSON字符串。
2. 点击"转换"按钮，JSON将在右侧以树形结构可视化。
3. 点击树节点上的+或-按钮以展开或折叠相应节点。
4. 使用"全部展开"/"全部折叠"按钮可一次性控制整个树。
5. 点击"示例数据"按钮自动输入样例JSON数据。
6. 点击"重置"按钮清除所有数据。

### 主题更改
- 点击侧边栏底部的"更改主题"按钮，可在亮色/暗色模式之间切换。

## 开发环境设置

```bash
# 安装开发用包
pip install -e ".[dev]"
```

## 未来计划

- 计划开发更多实用功能
- 性能优化
- 用户设置保存功能

## 许可证

本项目在MIT许可证下分发。详情请参阅[LICENSE](LICENSE)文件。

## 贡献

欢迎任何形式的贡献！您可以通过错误报告、功能请求或代码贡献来帮助改进这个项目。 