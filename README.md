# 💊 MedCabinet - 家庭药箱看板 
[English](#english) | [中文说明](#chinese)

---

<a name="english"></a> 
## 🇺🇸 English Overview

**MedCabinet** is an application designed to manage, track, and visualize home medications and first-aid supplies. Built with **Streamlit**, **Pandas**, and **Plotly**.

### Key Features
- **Bilingual Interface (ZH/EN)**: Instant toggling for all metrics, labels, forms, and charts.
- **Shelf-Life Feature Engineering**: Real-time dynamic calculation of expiration days left and risk level classification (Healthy >60d, Expiring Soon ≤60d, Expired <0d).
- **Interactive Data Science Visualizations**:
  - Expiry days remaining histogram with risk stratification.
  - Category and therapeutic distribution doughnut chart.
- **Dual-language Symptom Search**: Search medicines using common complaints in Chinese or English (e.g., `fever`, `头痛`, `allergy`, `拉肚子`).
- **Data Persistence**: Automatically reads and writes changes to `medicines.csv`.

### Quickstart (Local)
1. Clone the repository:
   ```bash
   git clone https://github.com/<YOUR_USERNAME>/<REPO_NAME>.git
   cd <REPO_NAME>
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

---

<a name="chinese"></a>
## 🇨🇳 中文说明

**MedCabinet** 是一个家庭常备药品监控系统，基于 **Streamlit**、**Pandas** 与 **Plotly** 构建。

### 核心功能
- **完整中英双语界面**：侧边栏随时切换，字段全自动双语展示。
- **效期特征工程**：基于系统当前时间动态计算每种药品的剩余保质天数，划分为“正常”、“临期（60天内）”与“已过期”。
- **交互式数据可视化**：
  - 剩余保质天数分布直方图（按风险区间聚类）。
  - 药品功效适应症结构占比图。
- **中英双语逆向症状检索**：可根据身体突发症状模糊检索可用药物（如搜索“发热”、“头痛”、“过敏”、“腹泻”）。
- **CSV 本地持久化储存**：随时通过表单登记新药或删除旧药，数据自动同步写入 `medicines.csv`。

### 免费公网部署指南 (Streamlit Cloud)
1. 将当前项目推送至你的 GitHub 仓库。
2. 访问 [Streamlit Community Cloud](https://share.streamlit.io/) 并使用 GitHub 账号登录。
3. 点击 **"New app"**，选择此仓库。
4. 主运行文件指定为 `app.py`，点击 **Deploy** 即可在一分钟内获得公网访问网址。
