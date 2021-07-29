echo 'enter filename to run'
read filename

typescript = "${filename}.ts"
javascript = "${filename}.js"

tsc $typescript && node $javascript
echo 'Done'
