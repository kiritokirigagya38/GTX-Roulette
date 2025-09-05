# 🎲 Bot Discord Roulette Valorant

## ⚙️ Installation locale

### 1. Cloner le projet
```bash
git clone https://github.com/ton-compte/discord-roulette-bot.git
cd discord-roulette-bot
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Configurer le bot
- Crée un fichier `.env` à la racine :
  ```
  DISCORD_TOKEN=ton_token_ici
  ```
- Dans `config.json`, règle le préfixe (`!` par défaut).

### 4. Lancer le bot
```bash
python bot.py
```

## 🚀 Déploiement sur Render
- Type de service : **Background Worker**
- Start command : `python bot.py`
- Variables d’environnement :
  - `DISCORD_TOKEN` = ton token Discord
