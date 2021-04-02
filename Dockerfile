ARG JEKYLL_VERSION

FROM jekyll/jekyll:${JEKYLL_VERSION}
ADD . /tmp/jekyll-site
WORKDIR /tmp/jekyll-site
RUN chown -R jekyll .
RUN jekyll build

FROM nginx:alpine
COPY --from=0 /tmp/jekyll-site/_site/ /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d
