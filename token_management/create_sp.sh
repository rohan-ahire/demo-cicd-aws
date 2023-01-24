curl -X POST \
${DATABRICKS_HOST}/api/2.0/preview/scim/v2/ServicePrincipals \
--header "Content-type: application/scim+json" \
--header "Authorization: Bearer ${DATABRICKS_TOKEN}" \
--data @create-service-principal.json \
| jq .