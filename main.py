""" main.py

    Required packages:
    - flask
    - folium

    Usage:
    Start the flask server by running:
        $ python main.py

    And then head to http://127.0.0.1:5000/ in your browser to see the map displayed
    Example taken from: https://python-visualization.github.io/folium/latest/advanced_guide/flask.html
"""

from flask import Flask, render_template_string, render_template

import folium
import pandas as pd

from database import Database

app = Flask(__name__)
db = Database()

@app.route("/")
def iframe():
    """Embed a map as an iframe on a page."""
    m = folium.Map(location=(50.0348411, 15.7775986))

    for church in db.get_list():
        folium.Marker(
            [church.lat, church.lon], 
            popup=f'{church.name}\n{church.closest_mass}',
            # icon=folium.Icon(icon="church")
        ).add_to(m)

    # set the iframe width and height
    # m.get_root().width = "800px"
    m.get_root().height = "600px"
    iframe = m.get_root()._repr_html_()

    return render_template(
        'index.html',
        iframe=iframe,
    )


# @app.route("/components")
# def components():
#     """Extract map components and put those on a page."""
#     m = folium.Map(
#         width=800,
#         height=600,
#         location=(50.0348411, 15.7775986)
#     )

#     m.get_root().render()
#     header = m.get_root().header.render()
#     body_html = m.get_root().html.render()
#     script = m.get_root().script.render()

#     return render_template_string(
#         """
#             <!DOCTYPE html>
#             <html>
#                 <head>
#                     {{ header|safe }}
#                 </head>
#                 <body>
#                     <h1>Using components</h1>
#                     {{ body_html|safe }}
#                     <script>
#                         {{ script|safe }}
#                     </script>
#                 </body>
#             </html>
#         """,
#         header=header,
#         body_html=body_html,
#         script=script,
#     )


if __name__ == "__main__":
    app.run(debug=True)