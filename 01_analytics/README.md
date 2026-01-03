# 01_analytics Directory

このディレクトリは、note記事のアクセス解析・分析データを管理します。

## 構造

- **00_method/**
    - 分析手法、計算式、マニュアルなどを格納
    - 例: `engagement_rate_method.md` (エンゲージメント率算出方法)
- **01_data/**
    - 生データ（CSVなど）を格納
    - 例: `2025-analytics.csv`
- **02_scripts/**
    - 分析用スクリプトを格納
    - 例: `calculate_engagement.py` (実行時はこのディレクトリ内で `python3 calculate_engagement.py` を実行)
- **03_reports/**
    - 分析結果のレポート、考察ログを格納
    - 例: `monthly_report_2025_jan.md`

## 運用ルール
- 新しいCSVデータをダウンロードしたら `01_data/` に配置してください。
- 分析レポートを作成した場合は `03_reports/` に保存してください。
