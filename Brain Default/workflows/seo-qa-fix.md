---
type: workflow
name: SEO QA và sửa
slug: seo-qa-fix
status: active
description: 'Audit một bài theo thứ tự: kiểm nguồn trước, rồi E-E-A-T, compliance và quy tắc của skill; sửa P0 và P1 thành bản _v2; kiểm lại.'
steps:
- agent: seo-auditor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | thư mục run | file bài trong run (mặc định draft.md) | từ khóa chính.
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Loại trang là dòng task trong RUN.md (blog, collection, product, refresh). Skill của loại trang và skill compliance ghi trong PROJECT.md. Đọc toàn bộ bài từ đầu. Audit đúng thứ tự sau, mỗi phần một mục trong báo cáo:
    1. Nguồn: nếu bài có link ngoài, số liệu hoặc trích dẫn thì chạy harry-reference-check (PASS, WARN, FAIL cho từng nguồn). Mọi link nội bộ phải có trong Projects/<slug>/data/inputs/site_urls.csv.
    2. E-E-A-T: chạy tapita-eeat-check với từ khóa chính và locale là market trong PROJECT.md.
    3. Compliance: skill compliance của khách (chế độ Audit) nếu PROJECT.md có; không có thì kiểm theo mục Từ cấm và claim cấm trong PROJECT.md.
    4. Quy tắc của skill viết của loại trang: độ dài, cấu trúc, vị trí từ khóa, độ dài meta theo đúng skill đó (đếm ký tự thật và ghi số). Collection có checklist trước khi giao trong skill thì đi hết checklist đó. Product: cột và quy tắc bảng theo skill.
    5. Nhãn còn sót: [CẦN NGUỒN], [CẦN SỐ LIỆU], SUBSTANTIATION NEEDED.
    Mỗi lỗi: vị trí (trích ngắn), vấn đề, mức P0 đến P3, cách sửa. Nguồn FAIL là P0 hoặc P1.
    Ghi review.md vào thư mục run (đã có thì ghi review_2.md).
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Bài: <đường dẫn file bài>
    Báo cáo: <đường dẫn file báo cáo>
    Số lỗi: P0=<n>, P1=<n>, P2=<n>, P3=<n>
- agent: seo-writer
  task: |-
    Kết quả bước trước: {{prev}}
    Mở file báo cáo và file bài nêu trong kết quả đó. Sửa mọi lỗi P0 và P1 theo giới hạn sửa của agent seo-writer. Ghi bản sửa thành file mới có hậu tố _v2 cạnh file bài (bài đã là _v2 thì ghi _v3).
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Bài sửa: <đường dẫn file mới>
    Báo cáo: <đường dẫn file báo cáo>
    Đã sửa: <số lỗi P0 và P1 đã xử lý>/<tổng số P0 và P1>
- agent: seo-auditor
  task: |-
    Kết quả bước trước: {{prev}}
    Đọc lại toàn bộ file bài sửa từ đầu. Kiểm lại từng lỗi P0 và P1 trong báo cáo cũ và quét lỗi mới phát sinh (đặc biệt khẳng định, số liệu hay nguồn mới). Ghi kết quả thành mục "Kiểm lại" ở cuối file báo cáo, kèm Verdict.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Người: duyệt <file bài sửa> (kiểm tay lại các link nguồn). Duyệt thì chép vào Projects/<slug>/deliverables/ và đặt status=approved; chưa đạt thì chạy lại seo-qa-fix trên file bài sửa" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Verdict: đạt hoặc không đạt
    Lỗi còn lại: <danh sách ngắn, hoặc không>
    Bản cuối: <đường dẫn file bài sửa>
updated: '2026-11-13'
---

Ba bước, một vòng sửa. Kiểm nguồn chạy trước E-E-A-T trong cùng một lượt audit vì nguồn sai kéo điểm Trust xuống. Dùng chung cho blog, collection, product (bảng meta và content) và bản refresh. Mỗi bước chỉ truyền vài dòng kết quả (đường dẫn file) sang bước sau. Theo sheet, người vẫn nên kiểm tay các link nguồn trước khi duyệt.
