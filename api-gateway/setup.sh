if ! command -v nginx &> /dev/null
then
    echo "nginx is not installed! Please install it."
    exit 1
fi

nginx_conf_path="$(nginx -V 2>&1 | grep -o '\-\-conf-path=\(.*conf\)' | cut -d '=' -f2)"
nginx_dir=$(dirname "$nginx_conf_path")

current_source_dir="$(dirname "${BASH_SOURCE[0]}")"

cp $current_source_dir/nginx.conf $nginx_dir
