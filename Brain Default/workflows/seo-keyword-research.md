---
type: workflow
name: SEO Keyword research
slug: seo-keyword-research
status: active
description: Tóm tắt dữ liệu từ khóa của khách rồi cluster và ghi clusters.csv. Cần có export Ahrefs hoặc GSC trong data/.
steps:
- agent: seo-extractor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | chủ đề hoặc seed keyword | thị trường.
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó.
    Đọc các file có trong Projects/<slug>/data/keywords/ (ahrefs_*.csv, clusters.csv), data/gsc/, data/rank/. Ghi tóm tắt (tối đa 50 dòng) vào Projects/<slug>/data/_summary/ theo hướng dẫn của agent seo-extractor. Nêu rõ file nào thiếu.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Tóm tắt: <đường dẫn>
    Đã đọc: <các file>
    Thiếu: <các file thiếu hoặc không>
- agent: seo-planner
  task: |-
    Kết quả bước trước: {{prev}}
    Mở file tóm tắt nêu trong đó và Projects/<slug>/data/keywords/clusters.csv hiện có. Cluster từ khóa theo chủ đề và intent, gắn target_url nếu đã có trang phù hợp trong data/inputs/site_urls.csv. Thêm hoặc cập nhật dòng trong clusters.csv (cột cluster, keyword, intent, volume, kd, target_url, status); thiếu volume hoặc kd thì để trống và ghi [CẦN SỐ LIỆU]. Không xóa dòng cũ. Ghi ghi chú quyết định vào Projects/<slug>/outputs/.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Clusters: <đường dẫn clusters.csv>
    Ghi chú: <đường dẫn file ghi chú>
    Việc cần người quyết: <ngắn, hoặc không>
updated: '2026-11-09'
---

Hai bước, chạy một lượt. Số liệu thiếu thì giữ trống chứ không ước lượng. Người xem clusters.csv và chốt từ khóa chính, phụ cho từng URL trước khi chạy `seo-content-brief`.
