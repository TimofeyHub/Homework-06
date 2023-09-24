from typing import Sequence

from flask import Blueprint, render_template, request, flash, redirect
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

from models.review import Review
from models.database import db

reviews_app = Blueprint(
    "reviews_app",
    __name__,
    url_prefix='/reviews'
)


@reviews_app.route("/", methods={"GET", "POST"}, endpoint="list")
def review_list():
    if request.method == "GET":
        stmt = select(Review).order_by(Review.id)
        reviews: Sequence[Review] = db.session.scalars(stmt)
        return render_template("review.html", reviews=reviews)

    review_text = request.form.get("review-text")
    if not review_text:
        raise BadRequest("Поле не должно быть пустым")

    review = Review(review_text=review_text)
    db.session.add(review)
    try:
        db.session.commit()
        return redirect(request.path)
    except IntegrityError:
        flash(f"Review with this text already exist", category="warning")
        return redirect(request.path)
