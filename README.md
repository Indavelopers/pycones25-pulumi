# PyConES'25 - Infraestructura como código en Python con Pulumi

## Ponente

- Marcos Manuel Ortega: <info@indavelopers.com>
- Consultor, arquitecto y formador - Director de Indavelopers
- Cloud computing, datos/ML/IA, devOps/IaC, finOps
- Google Cloud Authorized Trainer
- Google Developer Expert en Google Cloud
- (Ex)Co-organizador en múltiples comunidades tecnológicas: GDG Almería, GDG Cloud Español, DataBeers ALM, Hacklab Almería, Ideas for Almería...
- Fundador original del Club Python Almería: [Meetup](https://www.meetup.com/es-ES/python-almeria/), [logo](https://hacklabalmeria.net/recursos/logotipo-club-python.png)
- LinkedIn: [linkedin.com/in/marcosmanuelortega](https://www.linkedin.com/in/marcosmanuelortega/)
- GitHub: [github.com/Indavelopers](https://github.com/Indavelopers)

## Contenido

### ¿Qué vas a aprender?

1. ¿Qué es la IaC?
2. Workflow completo de IaC con Pulumi
3. Demo: webapp sobre Kubernetes en Google Cloud con IaC
4. "GCP training projects": IaC para crear entornos en la nube para formación o talleres

**DISCLAIMER:** Algunos ejemplos pueden no tener sentido a nivel de arquitectura

### Esta charla es para ti si piensas en

1. Crecer profesionalmente
2. Avanzar en el devOps/SRE/ingeniería de plataforma
3. Automatizar tu infraestructura
4. Abandonar Terraform

**CALL TO ACTION**: "La oportunidad de iniciarte en IaC utilizando tu lenguaje de desarrollo actual: Python"

### Intro a la automatización de infraestructura en devOps

Notas:

- dev &rarr; devOps &rarr; devSecOps
  - devOps = ing. SW automatiza Ops: entrega continua y ágil, operaciones, infraestructura
  - clickOps &rarr; script Bash &rarr; script Python &rarr; **IaC** &rarr; CI/CD &rarr; gitOps? &rarr; platform engineering??
  - **Clave:** imperativo vs declarativo
- IaC: "Infrastructure as Code"
  - Automatizar infraestructura - *no aplicaciones*
  - Despliegue, evolución, pruebas, replicación, recuperación de desastres (DR)
  - Plantilla declarativa: repetitividad, reusabilidad, composición, abstracción
  - Inmutabilidad, idempotencia, dependencias
  - Versionable, validable
  - Estandarización
  - Colaborar
- Alternativas IaC:
  - Terraform: <https://www.terraform.io/> ([no open source](https://github.com/hashicorp/terraform/commit/b145fbcaadf0fa7d0e7040eac641d9aef2a26433))
  - OpenTofu: <https://opentefu.org>
  - AWS CloudFormation: <https://aws.amazon.com/cloudformation>
  - AWS CDK: <https://aws.amazon.com/cdk>
  - Crossplane: <https://crossplane.io>
  - ...

### Pulumi

- Pulumi IaC: <https://www.pulumi.com/product/infrastructure-as-code/>
- Pulumi IaC OSS: <https://github.com/pulumi/pulumi>
- Pulumi registry: <https://www.pulumi.com/registry>
- Pulumi Google Cloud provider: <https://www.pulumi.com/registry/packages/gcp/>
- Convert from Terraform: <https://www.pulumi.com/blog/pulumi-convert-terraform-improvements/>

### Guía IaC con Pulumi

Carpetas:

- `examples`
- `example_stacks`

### Demo

Carpeta `infra_k8s_webapp`

## GCP training projects

- Herramienta OSS para crear múltiples proyectos de Google Cloud para formación o talleres con IaC
- Configura un proyecto para cada alumno, con facturación, APIs habilitadas, roles asignados y recursos creados por defecto
- Creada con Pulumi, Python y ❤️
- GH repo: <https://github.com/Indavelopers/gcp-training-projects>

## Agradecimientos

- Carlos Valdés ([LinkedIn](https://www.linkedin.com/in/carlosfcovaldeslopez/))
- Adrián Alonso Vega ([LinkedIn](https://www.linkedin.com/in/adrianalonsovega/))
