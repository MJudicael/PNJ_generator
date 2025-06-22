import sys
import random
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QPushButton, QVBoxLayout, QHBoxLayout,
                             QWidget)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class GenerateurPNJ(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configuration de la fenêtre
        self.setWindowTitle("Generateur de PNJ")
        self.setFixedSize(800, 600)

        # Widget central et layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)

        # Bouton de création
        self.btn_creation = QPushButton("Création")
        self.btn_creation.clicked.connect(self.lancement)
        self.main_layout.addWidget(self.btn_creation)

        # Initialisation des labels pour stocker les résultats
        self.labels = {}
        self.init_labels()

    def init_labels(self):
        """Initialise tous les labels nécessaires"""
        labels_info = {
            'info_base': ['Sexe:', 'Age:', 'Race:'],
            'caracteristiques': ['d20 Particularité du PNJ', 'd06 Caractéristique Haute',
                               'd06 Caractéristique Basse', 'd20 Talents du PNJ',
                               'd20 Manies du PNJ', 'd12 Traits d\'intéraction',
                               'd06 Idéal du Bien', 'd06 Idéal du Mal',
                               'd06 Idéal de la loi', 'd06 Idéal du chaos']
        }

        # Création d'un layout grille pour les informations de base
        info_layout = QHBoxLayout()
        for i, label_text in enumerate(labels_info['info_base']):
            container = QWidget()
            layout = QHBoxLayout(container)
            
            label = QLabel(label_text)
            label.setFixedWidth(50)  # Largeur fixe pour aligner
            value_label = QLabel()
            value_label.setFixedWidth(100)  # Largeur fixe pour aligner
            
            self.labels[label_text] = value_label
            
            layout.addWidget(label)
            layout.addWidget(value_label)
            layout.setContentsMargins(10, 0, 10, 0)  # Marges pour l'espacement
            
            info_layout.addWidget(container)
        
        self.main_layout.addLayout(info_layout)
        self.main_layout.addSpacing(20)  # Espace entre les sections

        # Création des autres labels avec alignement
        for text in labels_info['caracteristiques']:
            container = QWidget()
            layout = QHBoxLayout(container)
            
            label = QLabel(text)
            label.setFixedWidth(200)  # Largeur fixe pour aligner
            value_label = QLabel()
            value_label.setFixedWidth(200)  # Largeur fixe pour aligner
            
            self.labels[text] = value_label
            
            layout.addWidget(label)
            layout.addWidget(value_label)
            layout.addStretch()  # Pousse le contenu vers la gauche
            layout.setContentsMargins(20, 0, 20, 0)  # Marges pour l'espacement
            
            self.main_layout.addWidget(container)

    def lancement(self):
        """Génère et affiche les caractéristiques du PNJ"""
        # Listes de données
        donnees = {
            'Sexe:': ["Homme", "Femme"],
            'Race:': ["Orc", "Humain", "Nain", "Elfe", "Gnome"],
            'Age:': ["Enfant", "Adolescent", "Adulte", "Ancien", "Veillard"],
            'd20 Particularité du PNJ': ["Bijoux distinctifs", "Percings", "Vêtements extravagants"],
            'd06 Caractéristique Haute': ["Force", "Dextérité", "Constitution", "Intelligence", "Sagesse", "Charisme"],
            'd06 Caractéristique Basse': ["Force", "Dextérité", "Constitution", "Intelligence", "Sagesse", "Charisme"],
            'd20 Talents du PNJ': ["Joue d'un instrument", "Parle plusieurs langues", "Incroyablement chanceux"],
            'd20 Manies du PNJ': ["Chante souvent", "Parle en vers", "Voix particulière"],
            'd12 Traits d\'intéraction': list(range(1, 13)),
            'd06 Idéal du Bien': ["Beauté", "Charité", "Intérêt général"],
            'd06 Idéal du Mal': ["Domination", "Avarice", "Puissance"],
            'd06 Idéal de la loi': ["Communauté", "Equité", "Honneur"],
            'd06 Idéal du chaos': ["Changement", "Créativité", "Liberté"]
        }

        # Mise à jour des labels
        for key, values in donnees.items():
            if key in self.labels:
                value = str(random.choice(values))
                self.labels[key].setText(value)
                self.labels[key].setFont(QFont("Arial", 10, QFont.Bold))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GenerateurPNJ()
    window.show()
    sys.exit(app.exec())

