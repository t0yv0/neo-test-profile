import * as pulumi from "@pulumi/pulumi";
import * as service from "@pulumi/pulumiservice";

const deploymentSettings = new service.DeploymentSettings("my-deployment-settings", {
    organization: "pulumi_local",
    project: "mystack1",
    stack: "stack1",
    // sourceContext: {
    //     git: {
    //         repoUrl: "https://github.com/my-org/my-repo",
    //         branch: "main"
    //     }
    // },
    operationContext: {
        environmentVariables: {
            MY_ENV_VAR: "my-env-var-value"
        }
    }
});

export const result = 1;
export const myEnvVar = process.env.MY_ENV_VAR || "default-my-env-var-value";
