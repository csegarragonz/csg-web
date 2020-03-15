FROM jekyll/jekyll:latest
ADD . /tmp/jekyll-site
WORKDIR /tmp/jekyll-site
RUN jekyll build

FROM nginx:alpine
COPY --from=0 /tmp/jekyll-site/_site/ /usr/share/nginx/html
COPY ./privkey.pem /etc/letsencrypt/live/carlossegarra.com/ 
COPY ./fullchain.pem /etc/letsencrypt/live/carlossegarra.com/ 
COPY ./nginx.conf /etc/nginx/conf.d
