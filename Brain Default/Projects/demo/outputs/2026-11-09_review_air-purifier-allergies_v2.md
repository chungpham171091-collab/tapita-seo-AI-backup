# Báo cáo audit lần 3: Air Purifier for Allergies (demo)

**Bài kiểm:** Projects/demo/outputs/2026-11-08_draft_air-purifier-allergies_v2.md (bản cuối theo kết quả lần trước; đã đọc lại toàn bộ từ đầu, 110 dòng)
**Từ khóa chính:** air purifier for allergies | **Thị trường:** en-GB (registry, PROJECT.md và front matter của bài đều ghi en-GB; đầu vào lượt này ghi en-US, xem P3-1)
**Căn cứ:** Projects/SEO-OPS.md, Projects/demo/PROJECT.md (từ cấm và claim cấm), tapita-eeat-check, harry-reference-check. Cột compliance của demo trống, nên áp mục "Từ cấm và claim cấm" trong PROJECT.md.

Bài v2 không đổi so với lần kiểm trước: các dòng 10, 16, 20, 39, 102, 106, 110 vẫn như cũ.

## Kiểm tra định lượng (đếm thật)

- Meta title: 45 ký tự (đạt, 40–60).
- Meta description: 155 ký tự (đạt, 140–160).
- Độ dài: khoảng 1.520 từ phần thân (đạt, sát ngưỡng 1.500; phải đếm lại khi thay placeholder).
- "air purifier for allergies": 8 lần kể cả meta và H1 (không nhồi).
- Từ cấm ("medical grade", "100%", "guaranteed", claim chữa bệnh): không còn. "cure" chỉ nằm trong câu phủ định (dòng 18, 92).
- Placeholder [CẦN ...] còn lại: 14 dòng.
- Không có URL, DOI hay trích dẫn nào trong bài, nên harry-reference-check không có gì để fetch. Pass: 0 | Fail: 0 | Chưa có nguồn: 14 placeholder.

## Lỗi

| # | Vị trí (trích) | Vấn đề | Mức | Cách sửa |
|---|---|---|---|---|
| 1 | Dòng 10 "By [CẦN: author name and bio]"; dòng 102 "[CẦN: product specifications ... Do not publish until each figure has a source.]"; dòng 106 "[CẦN: store contact details, returns policy and warranty terms, with links]"; còn các [CẦN] ở dòng 34, 51, 96 | E-E-A-T chưa đạt cho chủ đề sức khỏe (QRG: thiếu tác giả, thiếu thông tin cửa hàng, thiếu thông số thật thì Experience, Expertise và Trust đều yếu). Chính bài cũng ghi "Do not publish". | P1 | Người điền: tên tác giả và tiểu sử liên quan, thông số sản phẩm kèm nguồn nhà sản xuất, liên hệ và chính sách đổi trả có link. Không bịa thông tin. |
| 2 | Dòng 16 "Many common allergy triggers are airborne particles: pollen..., pet dander, dust mite debris and mould spores. A purifier with a suitable filter can capture some of these"; dòng 20 "Allergens that have already settled on bedding, carpets and soft furniture stay there until they are removed"; dòng 39 "a purifier tends to work best when its rated coverage matches the room" | Khẳng định thực tế cụ thể, không nguồn và không gắn [CẦN NGUỒN] (SEO-OPS mục 4). Đây là lỗi N1 lần trước, chưa sửa. Dòng 16 và 20 liên quan sức khỏe nên cần nguồn rõ. | P1 | Thêm nguồn thật đã mở được, hoặc gắn [CẦN NGUỒN] ở cuối từng đoạn để người bổ sung. |
| 3 | Dòng 110 "get in touch with your room size so we can help you choose" | Câu kết sai ngữ nghĩa ("get in touch with your room size"). Lỗi N2 lần trước, chưa sửa. | P2 | Viết lại câu cuối cho rõ nghĩa, ví dụ nêu rõ người đọc gửi thông tin phòng cho cửa hàng (chỉ sau khi dòng 106 có thông tin liên hệ thật). |
| 4 | Dòng 51 "...which is when many people spend the most time indoors" (nói về giờ ngủ); dòng 65 "people spend many hours there with the door closed" | Khẳng định về thói quen người dùng, không nguồn, không đánh dấu. Ý "ngủ là lúc ở trong nhà nhiều nhất" cũng lủng củng. | P2 | Bỏ vế đó, hoặc nêu cụ thể và gắn [CẦN NGUỒN]. |
| 5 | Dòng 61 "Pet owners often find that dander is the trigger that is hardest to control" | Khẳng định kinh nghiệm chung, không nguồn. | P2 | Gắn [CẦN NGUỒN] hoặc đổi thành lời khuyên không kèm nhận định về số đông. |
| 6 | Đầu vào lượt này ghi thị trường en-US; registry, PROJECT.md và bài (front matter, chính tả "metres", "mould", "odour") đều là en-GB | Lệch thông tin thị trường giữa đầu vào và dữ liệu khách. | P3 | Xác nhận lại thị trường. Nếu đúng là en-GB (khả năng cao theo registry) thì giữ nguyên bài; nếu đổi sang en-US phải chuyển chính tả và đơn vị. |

## Ghi chú

- Kiểm tra kỹ thuật (crawl, index, schema, tốc độ) ngoài phạm vi, không kiểm.
- Phần compliance: không còn vi phạm. Không có thêm lỗi mới so với lần trước ngoài #4, #5 (P2, mức nhẹ).

## Verdict: KHÔNG ĐẠT

Không còn P0. Còn 2 P1 (#1, #2). Theo SEO-OPS, chỉ đạt khi không còn P0 và P1.

## Tóm tắt 5 dòng

1. Không còn P0: hết claim y tế, số liệu hiệu suất, từ cấm và link giả.
2. Meta title 45 ký tự, meta description 155 ký tự, thân bài khoảng 1.520 từ: đều đạt.
3. P1 còn lại: E-E-A-T (tác giả, thông số, thông tin cửa hàng vẫn là placeholder, bài tự ghi "Do not publish").
4. P1 còn lại: dòng 16, 20, 39 thiếu nguồn và thiếu nhãn [CẦN NGUỒN].
5. P2: câu kết dòng 110 sai nghĩa, dòng 51, 65, 61 có nhận định không nguồn. P3: đầu vào ghi en-US, dữ liệu khách là en-GB.

## Kiểm lại (sau bước sửa)

**Phạm vi:** đã đọc lại toàn bộ cả `_v2` (110 dòng) và `_v3` (110 dòng) từ đầu. `_v2` không đổi so với báo cáo trên. Bước sửa ghi ra `Projects/demo/outputs/2026-11-08_draft_air-purifier-allergies_v3.md`, nên bản cuối thật sự là `_v3`; kết quả kiểm lại dưới đây áp dụng cho `_v3`. Thị trường: en-GB (khớp registry và front matter).

| Lỗi cũ | Kết quả | Bằng chứng |
|---|---|---|
| P1 #2 (dòng 16, 20, 39 thiếu nguồn, thiếu nhãn) | Đã sửa (ở `_v3`); `_v2` vẫn lỗi | `_v3` dòng 16 "[CẦN NGUỒN: airborne allergen types...]", dòng 20 "[CẦN NGUỒN: settled allergens and cleaning]", dòng 39 "[CẦN NGUỒN: matching rated coverage to room size]". Nhãn này là đánh dấu thiếu nguồn, chưa phải nguồn thật: cần người bổ sung trước khi đăng. |
| P1 #1 (tác giả, thông số, thông tin cửa hàng) | Chưa sửa | Dòng 10 "By [CẦN: author name and bio]", dòng 102 "[CẦN: product specifications ... Do not publish until each figure has a source.]", dòng 106 "[CẦN: store contact details, returns policy and warranty terms, with links]". Cần người điền dữ liệu thật. |

**Quét lỗi mới:** không phát sinh P0/P1 mới. `_v3` chỉ khác `_v2` ở 3 nhãn trên. Không còn từ cấm hay claim chữa bệnh; không có URL/DOI/trích dẫn. Meta title 45 ký tự, meta description 155 ký tự (không đổi, đạt). Nhãn [CẦN ...] còn lại: 17 dòng.

**Lỗi P2/P3 chưa xử lý (không chặn Verdict):** dòng 110 "get in touch with your room size" (P2); dòng 51, 61, 65 nhận định không nguồn, chưa gắn nhãn (P2); đầu vào ghi en-US trong khi dữ liệu khách là en-GB (P3).

**Verdict sau kiểm lại: KHÔNG ĐẠT.** Còn 1 P1 (#1). Chỉ đạt khi người điền đủ tác giả, thông số có nguồn và thông tin cửa hàng, và các nhãn [CẦN NGUỒN] được thay bằng nguồn thật.
