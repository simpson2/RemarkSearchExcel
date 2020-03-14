from getVATSIM import getvatsim
import tablib
from pathlib import Path

output_dir = Path("../output")
file_to_open = output_dir / "output.xlsx"

dataset = tablib.Dataset()
dataset.headers = ["Pilot Name", "Pilot CID", "Pilot Remarks"]


def converttoexcel():

    jdata = getvatsim()

    for key in jdata:

        dataset.append([jdata[key]["name"],
                        jdata[key]["cid"],
                        jdata[key]["remarks"]])

    with open(file_to_open, "wb") as f:
        f.write(dataset.export("xlsx"))
        print("Write successful -> output/output.xlsx")
        f.close()


converttoexcel()
