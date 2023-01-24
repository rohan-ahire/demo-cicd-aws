curl -X POST \
${DATABRICKS_HOST}/api/2.0/token-management/on-behalf-of/tokens \
--header "Content-type: application/json" \
--header "Authorization: Bearer ${DATABRICKS_TOKEN}" \
--data @create-service-principal-token.json \
| jq .