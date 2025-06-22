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
        self.setFixedSize(470, 600)

        # Widget central et layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)

        # Bouton de création
        self.btn_creation = QPushButton("Création")
        self.btn_creation.setFont(QFont("Arial", 10, QFont.Bold))
        self.btn_creation.setStyleSheet("background-color: lightblue; color: black;")
        self.btn_creation.setFixedWidth(80) # Largeur fixe pour aligner         
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
                               'd20 Manies du PNJ', 'd06 Idéal du Bien', 
                               'd06 Idéal du Mal', 'd06 Idéal de la loi', 
                               'd06 Idéal du chaos']
        }

        # Style commun pour les labels de base
        base_label_style = """
            QLabel {
                background-color: #f0f0f0;
                border: 1px solid #c0c0c0;
                border-radius: 5px;
                padding: 5px;
                text-align: center;
                color: black;
            }
        """

        # Style commun pour les labels des caractéristiques
        carac_label_style = """
            QLabel {
                background-color: #f0f0f0;
                border: 1px solid #c0c0c0;
                border-radius: 5px;
                padding: 5px;
                text-align: center;
                color: black;
            }
        """

        # Création d'un container pour aligner verticalement les informations de base
        base_container = QWidget()
        base_layout = QHBoxLayout(base_container)
        base_layout.setContentsMargins(20, 5, 20, 5)

        # Layout vertical pour les labels et les valeurs
        labels_layout = QVBoxLayout()
        values_layout = QVBoxLayout()

        for label_text in labels_info['info_base']:
            label = QLabel(label_text)
            label.setFixedWidth(50)
            label.setAlignment(Qt.AlignCenter)  # Centrage du texte du label
            label.setStyleSheet(base_label_style)
            
            value_label = QLabel()
            value_label.setFixedWidth(100)
            value_label.setAlignment(Qt.AlignCenter)  # Centrage du texte de la valeur
            value_label.setStyleSheet(base_label_style)
            
            self.labels[label_text] = value_label
            
            labels_layout.addWidget(label)
            values_layout.addWidget(value_label)

        base_layout.addLayout(labels_layout)
        base_layout.addLayout(values_layout)
        base_layout.addStretch()
        
        self.main_layout.addWidget(base_container)
        self.main_layout.addSpacing(20)

        # Création des autres labels avec alignement et encadrement
        for text in labels_info['caracteristiques']:
            container = QWidget()
            layout = QHBoxLayout(container)
            
            label = QLabel(text)
            label.setFixedWidth(200)
            label.setStyleSheet(carac_label_style)
            label.setAlignment(Qt.AlignCenter)
            
            value_label = QLabel()
            value_label.setFixedWidth(250)
            value_label.setAlignment(Qt.AlignCenter)
            
            self.labels[text] = value_label
            
            layout.addWidget(label)
            layout.addWidget(value_label)
            layout.addStretch()
            layout.setContentsMargins(20, 5, 20, 5)
            
            self.main_layout.addWidget(container)

    def lancement(self):
        """Génère et affiche les caractéristiques du PNJ"""
        # Listes de données
        donnees = {
            'Sexe:': ["Homme", "Femme"],
            'Race:': ["Orc", "Humain", "Nain", "Elfe", "Gnome"],
            'Age:': ["Enfant", "Adolescent", "Adulte", "Ancien", "Veillard"],
            'd20 Particularité du PNJ': ["Avec des bijoux distinctifs", "Avec des percings", "Avec des vêtements extravagants"],
            'd06 Caractéristique Haute': ["Force", "Dextérité", "Constitution", "Intelligence", "Sagesse", "Charisme"],
            'd06 Caractéristique Basse': ["Force", "Dextérité", "Constitution", "Intelligence", "Sagesse", "Charisme"],
            'd20 Talents du PNJ': ["Joue d'un instrument", "Parle plusieurs langues", "Incroyablement chanceux"],
            'd20 Manies du PNJ': ["Chante souvent", "Parle en vers", "Voix particulière"],
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

