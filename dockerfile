FROM golang:1.19

WORKDIR /usr/src/app

# pre-copy/cache go.mod for pre-downloading dependencies and only redownloading them in subsequent builds if they change
COPY go.mod go.sum ./
RUN go mod tidy

RUN  go env -w GO111MODULE=on
RUN go env -w GOPROXY=https://goproxy.cn,direct


COPY . .
RUN go build -v -o /usr/local/bin/app ./...

CMD ["app"]
