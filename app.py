from flask import Flask, render_template

app = Flask(__name__)

@app.route('/cgv')
def cgv():
    return render_template('cgv.html')

@app.route('/cgu')
def cgu():
    return render_template('cgu.html')
@app.route('/')
def index():
    import os
    gallery_path = os.path.join(app.static_folder, 'gallery_confiance')
    images = [f for f in os.listdir(gallery_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('index.html', images=images)
@app.route('/politique_cookies')
def politique_cookies():
    return render_template('politique_cookies.html')

@app.route('/politique_confidentialite')
def politique_confidentialite():
    return render_template('politique_confidentialite.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/gallery')
def gallery():
    import os
    gallery_path = os.path.join(app.static_folder, 'gallery')
    images = [f for f in os.listdir(gallery_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    print("Gallery images:", images)  # Debug
    return render_template('gallery.html', images=images)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/mentions')
def mentions():
    return render_template('mentions.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/sonorisation')
def sonorisation():
    return render_template('sonorisation.html')

@app.route('/lumieres')
def lumieres():
    return render_template('lumieres.html')

@app.route('/animation_musicale')
def animation_musicale():
    return render_template('animation_musicale.html')

@app.route('/engagement_ecoresponsable')
def engagement_ecoresponsable():
    return render_template('engagement_ecoresponsable.html')
@app.route('/prestations_sur_mesure')
def prestations_sur_mesure():
    return render_template('prestations_sur_mesure.html')

@app.route('/conseil_coaching')
def conseil_coaching():
    return render_template('conseil_coaching.html')

@app.route('/video_projection')
def video_projection():
    return render_template('video_projection.html')

@app.route('/animation_interactive')
def animation_interactive():
    return render_template('animation_interactive.html')
