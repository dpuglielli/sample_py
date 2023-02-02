# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.217.4/containers/dotnet/.devcontainer/base.Dockerfile

# [Choice] .NET version: 6.0, 5.0, 3.1, 6.0-bullseye, 5.0-bullseye, 3.1-bullseye, 6.0-focal, 5.0-focal, 3.1-focal
ARG VARIANT="6.0-bullseye-slim"
FROM mcr.microsoft.com/vscode/devcontainers/dotnet:0-${VARIANT}

ARG HADOLINT_VERSION=v2.8.0
# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi


RUN /bin/bash -c " set -o pipefail \
    && curl -L -q https://aquasecurity.github.io/trivy-repo/deb/public.key | \
       gpg --dearmor > /usr/share/keyrings/trivy.gpg \
    && echo deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | \
       tee -a /etc/apt/sources.list.d/trivy.list \
    && apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
      python3-pip=20.3.4-4+deb11u1 \
      vim=2:8.2.2434-3+deb11u1 \
      trivy \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir gcloud==0.18.3"

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1
ARG GCLOUD_VERSION=412.0.0
ARG GCLOUD_ARCH=x86_64

WORKDIR /usr/local/share
RUN /bin/bash -c "set -o pipefail \
    # Install hadolint
    && curl -L https://github.com/hadolint/hadolint/releases/download/v2.8.0/hadolint-Linux-x86_64 -o /usr/local/bin/hadolint \
    && chmod +x /usr/local/bin/hadolint \
    # Install gcloud
    && curl -L https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${GCLOUD_VERSION}-linux-${GCLOUD_ARCH}.tar.gz | tar xzf - \
    && echo NY | sh google-cloud-sdk/install.sh"

# Setup user environment
RUN echo ". /home/vscode/.oh-my-zsh/plugins/gitfast/git-completion.bash" >> /home/vscode/.bashrc \
    # bash aliases
    && echo "export PATH=\$PATH:/usr/local/share/google-cloud-sdk/bin" >> /home/vscode/.bashrc \
    && echo "alias gauth='gcloud auth login --update-adc --no-launch-browser'" >> /home/vscode/.bashrc \
    && echo "alias docker-here='docker run -it --rm -v \$PWD:/src -w /src'" >> /home/vscode/.bashrc \
    && echo "complete -C /usr/local/bin/terraform terraform" >> /home/vscode/.bashrc \
    && echo "alias tfsec='docker run --rm -it -v \"\${PWD}:/src\" aquasec/tfsec /src'" >> /home/vscode/.bashrc \
    # zsh aliases
    && echo "export PATH=\$PATH:/usr/local/share/google-cloud-sdk/bin" >> /home/vscode/.zshrc \
    && echo "alias gauth='gcloud auth login --update-adc --no-launch-browser'" >> /home/vscode/.zshrc \
    && echo "alias docker-here='docker run -it --rm -v \$PWD:/src -w /src'" >> /home/vscode/.zshrc \
    && echo "complete -C /usr/local/bin/terraform terraform" >> /home/vscode/.zshrc \
    && echo "alias tfsec='docker run --rm -it -v \"\${PWD}:/src\" aquasec/tfsec /src'" >> /home/vscode/.zshrc

USER vscode
