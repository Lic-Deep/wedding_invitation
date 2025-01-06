from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
def invitation():
    # 청첩장 정보
    couple_name = "이인찬 & 정도희"
    wedding_date = "2025년 6월 15일"
    wedding_time = "오후 12시"
    venue_name = "서울 잠실 더 컨밴션"
    venue_address = "서울특별시 송파구 올림픽로 319 3층"
    rsvp_contact = "010-4900-2916"
    bank_details = {
        "신랑 측": {"은행명": "국민은행", "계좌번호": "123-456-7890", "예금주": "이인찬"},
        "신부 측": {"은행명": "신한은행", "계좌번호": "987-654-3210", "예금주": "정도희"}
    }
    gallery_images = [
        url_for('static', filename='images/photo1.jpg'),
        url_for('static', filename='images/photo2.jpg'),
        url_for('static', filename='images/photo3.jpg'),
        url_for('static', filename='images/photo1.jpg'),
        url_for('static', filename='images/photo2.jpg'),
        url_for('static', filename='images/photo3.jpg'),
        url_for('static', filename='images/photo1.jpg'),
        url_for('static', filename='images/photo2.jpg'),
        url_for('static', filename='images/photo3.jpg'),
        url_for('static', filename='images/photo1.jpg'),
        url_for('static', filename='images/photo2.jpg'),
        url_for('static', filename='images/photo3.jpg'),
    ]

    return render_template(
        "invitation.html",
        couple_name=couple_name,
        wedding_date=wedding_date,
        wedding_time=wedding_time,
        venue_name=venue_name,
        venue_address=venue_address,
        rsvp_contact=rsvp_contact,
        bank_details=bank_details,
        gallery_images=gallery_images,
    )

@app.route("/gallery-container")
def gallery():
    images = [
        url_for('static', filename='images/photo1.jpg'),
        url_for('static', filename='images/photo2.jpg'),
        url_for('static', filename='images/photo3.jpg'),
    ]
    return render_template("gallery.html", images=images)

if __name__ == "__main__":
    app.run(debug=True)
