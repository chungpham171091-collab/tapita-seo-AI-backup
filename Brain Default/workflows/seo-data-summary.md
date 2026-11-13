---
type: workflow
name: SEO Tóm tắt dữ liệu theo kỳ
slug: seo-data-summary
status: 'off'
description: Extractor đọc file export thô của một nguồn, ghi bản tóm tắt của kỳ và ghi đè bản latest. Agent khác chỉ đọc bản latest.
steps:
- agent: seo-extractor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | nguồn (gsc, rank, ga4, keywords hoặc backlinks) | kỳ (YYYY-MM-DD là ngày cuối của tuần, YYYY-MM là tháng, hoặc "mới nhất").
    Đọc Projects/SEO-OPS.md mục 6 và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó.
    Đọc README trong Projects/<slug>/data/<nguồn>/ để biết tên file, rồi đọc file thô của kỳ (chỉ đọc, không sửa). Kỳ là "mới nhất" thì lấy file có ngày mới nhất trong thư mục.
    Với gsc và rank: so tổng 4 file tuần gần nhất với tổng 4 file tuần trước đó. Chưa đủ 8 file tuần thì nói rõ có bao nhiêu file và chỉ báo số của các tuần đang có, không ước lượng phần thiếu. Với ga4: so tháng này với tháng trước. Với keywords và backlinks: đếm và phân nhóm, không so kỳ.
    Ghi bản tóm tắt tối đa 50 dòng vào Projects/<slug>/data/_summary/<kỳ>_<nguồn>.md. Đầu file ghi: file nguồn đã đọc, kỳ dữ liệu, số dòng đã đọc, ngày tạo. Với gsc: tổng clicks, impressions, CTR, vị trí; các trang và query tăng, giảm nhiều nhất theo cửa sổ 4 tuần. Sau đó ghi đè Projects/<slug>/data/_summary/latest_<nguồn>.md bằng đúng nội dung đó.
    Liệt kê các file tuần trong thư mục nguồn cũ hơn 13 tuần vào cuối bản tóm tắt, mục "File cũ cần người quyết định". Không xóa, không chuyển file.
    Không đưa khuyến nghị. File thiếu hoặc rỗng thì dừng và báo file nào thiếu.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 5 dòng:
    Khách: <slug>
    Tóm tắt kỳ: <đường dẫn hoặc không có>
    Latest: <đường dẫn hoặc không có>
    Đã đọc: <các file>
    Thiếu hoặc file cũ: <ngắn, hoặc không>
updated: '2026-11-13'
---

Một bước. Chạy sau mỗi lần đặt file export mới vào data/: gsc và rank hằng tuần, ga4 hằng tháng, keywords hằng quý. Người xem mục "File cũ cần người quyết định" và tự chuyển file vào `_archive/`.
