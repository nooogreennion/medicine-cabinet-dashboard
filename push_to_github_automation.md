#!/bin/bash

# ==============================================================================
# Script to initialize Git, commit all files, and push to GitHub.
# Usage:
#   chmod +x push_to_github.sh
#   ./push_to_github.sh <YOUR_GITHUB_REPO_URL>
# Example:
#   ./push_to_github.sh https://github.com/myusername/medcabinet-dashboard.git
# ==============================================================================

REPO_URL=$1

if [ -z "$REPO_URL" ]; then
  echo "❌ Error: Please provide your GitHub repository URL as an argument."
  echo "Example: ./push_to_github.sh https://github.com/username/medcabinet-dashboard.git"
  exit 1
fi

echo "🚀 Step 1: Initializing git repository..."
git init

echo "📦 Step 2: Staging files..."
git add .

echo "✍️  Step 3: Committing initial code..."
git commit -m "feat: complete bilingual home medicine analytics project"

echo "🌿 Step 4: Setting main branch..."
git branch -M main

echo "🔗 Step 5: Setting remote origin to $REPO_URL..."
git remote remove origin 2>/dev/null
git remote add origin "$REPO_URL"

echo "⬆️  Step 6: Pushing code to GitHub..."
git push -u origin main

echo "✅ Done! Your code is now live on GitHub."