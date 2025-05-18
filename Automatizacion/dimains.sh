#!/bin/bash

# Directorio base
baseDir="/opt/BugBounty"

# Webhook de Discord
webhook_url="https://discord.com/api/webhooks/ID_DEL_WEBHOOK/TOKEN_DEL_WEBHOOK"

# Directorio del repositorio de GitHub
repoDir="/opt/BugBounty/reports"

if [[ -d "$baseDir" ]]; then
  for dir in "$baseDir"/*/; do
    if [[ -f "${dir}/roots.txt" ]]; then
      programName=$(basename "$dir")
      echo "Grabbing domains for $programName:"

      # Ejecuta subfinder y guarda los resultados en alldomains.txt
      subfinder -dL "${dir}/roots.txt" -silent | anew "${dir}/alldomains.txt" | notify -silent -bulk

      if [[ -f "${dir}/alldomains.txt" ]]; then
        # Leer dominios
        domains=$(cat "${dir}/alldomains.txt")

        # Comprimir el archivo de resultados
        tarball="${dir}/${programName}_$(date +%Y-%m-%d).tar.gz"
        tar -czf "$tarball" -C "$dir" "alldomains.txt"

        # Enviar reporte a Discord
        curl -X POST -H "Content-Type: application/json" \
             -F "file=@$tarball" \
             -F "payload_json={\"content\": \"Reporte de $programName:\"}" \
             "$webhook_url"

        # Subir reporte a GitHub
        cp "$tarball" "$repoDir/${programName}_$(date +%Y-%m-%d).tar.gz"

        cd "$repoDir" || exit
        git add "${programName}_$(date +%Y-%m-%d).tar.gz"
        git commit -m "Reporte comprimido para $programName - $(date)"
        git push origin main
      fi
    else
      programName=$(basename "$dir")
      echo "No root domains found for $programName!"
    fi
  done
else
  echo "Directory '$baseDir' does not exist."
fi
