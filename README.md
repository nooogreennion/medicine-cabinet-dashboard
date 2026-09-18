# 💊 MedCabinet - 家庭药箱数据库

### Smart Home Medicine Inventory & Shelf-Life Analytics Dashboard

[English](#-english) | [中文说明](#-中文说明)

## 🇺🇸 English

**MedCabinet** is a web application designed to track, organize, and analyze household medications.

By applying fundamental data science concepts (feature derivation, time-to-expiry risk stratification, categorical distribution, and reverse fuzzy symptom lookup), it helps families prevent accidental consumption of expired drugs and optimize first-aid preparedness.

### 🌟 Key Features

* **🌐 Bilingual Support (ZH / EN)**: Instant toggle between Chinese and English for all UI metrics, form elements, status tags, and chart legends.

* **⏱️ Dynamic Shelf-Life Feature Engineering**: Automatically computes days remaining until expiration against current local time:

  * 🟢 **Healthy / 安全**: > 60 days remaining

  * 🟡 **Expiring Soon / 临期**: ≤ 60 days remaining (priority refill or usage)

  * 🔴 **Expired / 已过期**: < 0 days (safe disposal warning)

* **📊 Interactive Data Visualizations (Chart.js)**:

  * **Expiry Timeline Bins (Histogram)**: Visualizes the lifecycle distribution of stocked drugs to prevent batch expirations.

  * **Therapeutic Category Ratio (Doughnut Chart)**: Analyzes the balance across categories (Analgesics, Antibiotics, Gastrointestinal, First Aid, etc.).

* **🔍 Reverse Symptom & Drug Search**: Fuzzy search that matches not only drug brand/generic names, but also symptoms in Chinese and English (e.g., `头痛`, `发烧`, `fever`, `allergy`, `cough`).

* **💾 Browser-Local Data Persistence**: Full CRUD support (Create, Read, Delete, Reset to demo data) using `localStorage`.

### 🚀 How to Run Locally

No server or Python installation required.

1. Clone or download this repository:

   ```
   git clone https://github.com/nooogreennion/medicine-cabinet-dashboard.git
   cd medicine-cabinet-dashboard
   
   ```

2. Double-click `index.html` to open directly in any modern web browser (Chrome, Safari, Edge, Firefox).

### 🌐 Live Demo & Deployment via GitHub Pages

This project is configured to run out-of-the-box on GitHub Pages:

1. Go to repository **Settings** > **Pages**.

2. Under **Build and deployment**, select **Deploy from a branch**.

3. Set branch to `main` and folder to `/ (root)`.

4. Click **Save** and wait \~1 minute for your live link.

## 🇨🇳 中文说明

**MedCabinet** 是一个纯前端驱动的轻量化家庭常备用药数据分析与保质期监控平台。

本项目将生物医药常识与数据分析流程相结合，实现了药品效期特征工程计算、剩余保质期风险分层、药谱分类统计与身体不适症状逆向检索，帮助家庭科学管理药箱，避免误服过期药物。

### 🌟 核心功能

* **🌐 完整中英文即时切换**：导航栏一键切换，指标卡、图表、表格与录入表单自适应中英双语。

* **⏱️ 效期衍生特征动态计算**：根据用户本地设备时间自动推算剩余保质期，划分三种健康风险级别：

  * 🟢 **充足安全**：剩余大于 60 天

  * 🟡 **临期预警**：剩余不足 60 天（优先采买或使用）

  * 🔴 **过期失效**：已过期（提示密封并作无害化安全处理）

* **📊 交互式数据可视化看板 (Chart.js)**：

  * **效期区间分布直方图**：呈现家庭备药生命周期阶段分布，避免批量过期损耗。

  * **功效分类环形图**：直观展示解热镇痛、抗感染、消化系统、外用急救等品类的储备平衡度。

* **🔍 双语智能症状匹配检索**：支持按药品名模糊搜索，同时支持直接输入身体不适症状（如输入“头痛”、“发热”、“拉肚子”、“fever”等）自动匹配适用药品。

* **💾 本地无感持久化存储**：采用浏览器 `localStorage` 存储药品明细，支持新增录入、删除及一键重置演示数据。

### 🚀 本地运行方式

本项目为纯静态结构，**无需安装任何 Python 运行环境或依赖包**：

1. 下载或克隆本仓库到本地电脑；

2. 直接双击打开 `index.html` 即可在浏览器中使用全部功能。

### 🌐 GitHub Pages 公网部署

1. 进入本 GitHub 仓库的 **Settings**（设置）；

2. 在左侧菜单点击 **Pages**；

3. **Source** 保持 `Deploy from a branch`，**Branch** 选择 `main` 分支，路径选择 `/(root)`；

4. 点击 **Save**，等待 1\~2 分钟即可获得专属公开网站链接。

### 📂 目录结构 (Project Structure)

```
medicine-cabinet-dashboard/
├── index.html       # 核心单文件网页应用 (HTML + TailwindCSS + Chart.js)
├── README.md        # 项目说明文档
└── .gitignore       # Git 忽略配置

```

### 🛠️ 技术栈 (Tech Stack)

* **HTML5 & Vanilla JavaScript (ES6+)**

* **Tailwind CSS (CDN)** - 现代化响应式医疗 UI 界面设计

* **Chart.js** - 响应式数据可视化图表

* **FontAwesome 6** - 医疗与操作图标集
