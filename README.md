[![Github Action](https://github.com/kitsudog/mongo-shake/actions/workflows/main.yml/badge.svg)](https://github.com/kitsudog/mongo-shake/actions/workflows/main.yml)
[![Docker Image Size](https://img.shields.io/docker/image-size/kitsudo/mongo-shake?sort=semver)](https://hub.docker.com/r/kitsudo/mongo-shake "Click to view the image on Docker Hub")
[![Docker stars](https://img.shields.io/docker/stars/kitsudo/mongo-shake.svg)](https://hub.docker.com/r/kitsudo/mongo-shake 'DockerHub')
[![Docker pulls](https://img.shields.io/docker/pulls/kitsudo/mongo-shake.svg)](https://hub.docker.com/r/kitsudo/mongo-shake 'DockerHub')

# Example
```
docker run --rm -it -e SRC_MONGO_URL=mongodb://mongoA/ -e DST_MONGO_URL=mongodb://mongoB/ -e SYNC_MODE=full kitsudo/mongo-shake
```