# Generating the code

Use the `swagger-codegen-cli`

```
java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate --additional-properties projectName=harbor_client --additional-properties packageVersion=2.7.0 --api-package harbor_client --config  --input-spec ~/Downloads/swagger.yaml --lang python --output harbor_client
```

Replace unwanted namings:

```
grep -rl swagger_client . | xargs sed -i 's/swagger_client/harbor_client/g'
grep -rl "from api" . | xargs sed -i 's/from api/from harbor_client.api./g'
```
