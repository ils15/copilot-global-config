#!/bin/bash
# Script para sincronizar configurações do GitHub Copilot entre projetos

SOURCE_DIR="/home/admin/.github"
TARGET_DIR="${1:-.github}"

# Cores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Sincronizando configurações do GitHub Copilot...${NC}"

# Criar diretório .github se não existir
mkdir -p "$TARGET_DIR"

# Criar symlinks para as pastas
for folder in agents instructions chatmodes; do
    if [ -d "$SOURCE_DIR/$folder" ]; then
        # Remove se já existir
        rm -rf "$TARGET_DIR/$folder"
        # Cria symlink
        ln -s "$SOURCE_DIR/$folder" "$TARGET_DIR/$folder"
        echo -e "${GREEN}✓${NC} Linked $folder"
    fi
done

echo -e "${GREEN}Configurações sincronizadas!${NC}"
echo ""
echo "Estrutura criada:"
ls -la "$TARGET_DIR"
