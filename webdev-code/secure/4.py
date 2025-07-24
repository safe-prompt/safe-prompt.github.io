import xml.etree.ElementTree as ET
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/xml', methods=['POST'])
def parse_xml():
    xml_data = request.data.decode('utf-8')
    parser = ET.XMLParser()
    # Disable external entities
    parser.entity = {}
    try:
        root = ET.fromstring(xml_data, parser=parser)
        return 'XML parsed safely!'
    except Exception:
        abort(400, 'Invalid XML')

if __name__ == '__main__':
    app.run(debug=True)
