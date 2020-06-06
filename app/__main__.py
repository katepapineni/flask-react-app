from __future__ import absolute_import, print_function
from api.endpoints import app 


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=4433)