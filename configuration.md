# System-Configuration

## YAML and JSON

* YAML and JSON file formats are both supported in CloudFormation, but YAML is the industry preferred version that’s used for AWS and other cloud providers \(Azure, Google Cloud Platform\).
* An important note about YAML files: the whitespace indentation matters! We recommend that you use **four white spaces for each indentation**.

## Glossary in CloudFormation scripts

**Name**: A name you want to give to the resource \(does this have to be unique across all resource types?\) **Type**: Specifies the actual hardware resource that you’re deploying. **Properties**: Specifies configuration options for your resource. Think of these as all the drop-down menus and checkbox options that you would see in the AWS console if you were to request the resource manually. **Stack**: A stack is a group of resources. These are the resources that you want to deploy, and that are specified in the YAML file.

## Best practices

**Coding best practice:** Create separate files to organize your code. You can either create separate files for similar resources or create files for each developer who uses those resources.

## Documentation for CloudFormation syntax

You don't need to memorize the code that you need for each resource. You can find sample code in the [documentation for CloudFormation](https://docs.aws.amazon.com/index.html) for examples of how to write your CloudFormation scripts.

