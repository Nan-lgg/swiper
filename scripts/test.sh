#!/bin/bash

a=123456789
echo a  # 作为字符串的 a
echo $a  # 作为变量的 a

echo 'echo 语句--------------------------------------------'

echo "----$a--\n--" # 无视转义字符
echo '----$a--\n--' # 无视转义字符

echo -e "----$a--\n--"  # 输出转义字符

echo 'printf 语句 ---------------------------------------'

printf "=====$a--\n--" # 识别转义字符，识别变量
printf '=====$a--\n--' # 识别转义字符，不识别变量

echo '全局变量-------------------------------------------'

export ABC=987654321


echo 'if 分支语句 ----------------------------------------'

if [[ -z ./test.sh ]]; then
    echo 'true'
elif [[ -f ./test.sh ]]; then
    echo '123456789'
else
    echo 'false'
fi


foo() {
    echo "参数0：$0"
    echo "参数1：$1"
    echo "参数2：$2"
    echo "参数3：$3"
    echo "参数4：$4"
    echo "参数5：$5"

    echo "全部参数：$*"

    echo "遍历"
    for arg in $@
    do
        echo $arg
    done

    echo "参数个数：$#"
}

foo  abc xyz def opq

echo "----------------------------------------------------------------"

echo "脚本参数0：$0"
echo "脚本参数1：$1"
echo "脚本参数2：$2"
echo "脚本参数3：$3"
echo "脚本参数4：$4"
echo "脚本参数5：$5"

echo "全部脚本参数：$*"

echo "遍历"
for arg in $@
do
    echo $arg
done

echo "脚本参数个数：$#"
