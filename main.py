import chevron
from datetime import datetime
from pytz import timezone
from pathlib import Path


FNAME = "Ci Leong"
LNAME = "Ong"

POSITION = "Software Engineer"
COMPANY = "Digicraft MSC Sdn. Bhd."

TIMEZONE = timezone("Asia/Kuala_Lumpur")
dt = datetime.now(TIMEZONE)
STATUS = (
    "Working 💻"
    if dt.isoweekday() in range(1, 6) and dt.hour in range(9, 18)
    else "Off work 💤"
)


DATA = {
    "fname": FNAME.title(),
    "lname": LNAME.upper(),
    "position": POSITION.title(),
    "company": COMPANY,
    "status": STATUS.capitalize(),
}


if __name__ == "__main__":

    TEMPLATE_PATH = Path(__file__).parent / "template.mustache"
    README_PATH = Path(__file__).parent / "README.md"

    with TEMPLATE_PATH.open("r") as t, README_PATH.open("w") as r:
        r.write(chevron.render(t, DATA))
