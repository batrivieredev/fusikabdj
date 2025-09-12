from flask import Flask, render_template
import os

app = Flask(__name__)

# Pages légales
@app.route('/cgv')
def cgv():
    return render_template('cgv.html')

@app.route('/cgu')
def cgu():
    return render_template('cgu.html')

@app.route('/politique_cookies')
def politique_cookies():
    return render_template('politique_cookies.html')

@app.route('/politique_confidentialite')
def politique_confidentialite():
    return render_template('politique_confidentialite.html')

@app.route('/mentions')
def mentions():
    return render_template('mentions.html')

# Pages principales
@app.route('/')
def index():
    gallery_path = os.path.join(app.static_folder, 'gallery_confiance')
    images = [f for f in os.listdir(gallery_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('index.html', images=images)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/gallery')
def gallery():
    gallery_path = os.path.join(app.static_folder, 'gallery')
    images = [f for f in os.listdir(gallery_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('gallery.html', images=images)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

# Pages services individuelles
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

# Pages partenaires
@app.route('/partenaire1_sallele5B')
def partenaire1_sallele5B():
    images_path = os.path.join(app.static_folder, 'images/partenaire1_sallele5B')
    images = [f for f in os.listdir(images_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('partenaire/partenaire1_sallele5B.html', images=images)

@app.route('/partenaires')
def partenaires():
    return render_template('partenaire/index_partenaires.html')

@app.route('/partenaire2_chateau')
def partenaire2_chateau():
    images_path = os.path.join(app.static_folder, 'images/partenaire2_chateau')
    images = [f for f in os.listdir(images_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('partenaire/partenaire2_chateau.html', images=images)

@app.route('/partenaire3_photographe')
def partenaire3_photographe():
    images_path = os.path.join(app.static_folder, 'images/partenaire3_photographe')
    images = [f for f in os.listdir(images_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('partenaire/partenaire3_photographe.html', images=images)

@app.route('/partenaire4_traiteur')
def partenaire4_traiteur():
    images_path = os.path.join(app.static_folder, 'images/partenaire4_traiteur')
    images = [f for f in os.listdir(images_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('partenaire/partenaire4_traiteur.html', images=images)

@app.route('/partenaire5_deco')
def partenaire5_deco():
    images_path = os.path.join(app.static_folder, 'images/partenaire5_deco')
    images = [f for f in os.listdir(images_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('partenaire/partenaire5_deco.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)
