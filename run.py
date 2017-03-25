# -*- coding: utf-8 -*-
#!/usr/bin/env python

from app import app


@app.route("/")
def show_start_atable():
	table = {u"Пакет":u"моделью", u"создали":""}
	return render_template('index.html', table=table)

app.run(debug=True)