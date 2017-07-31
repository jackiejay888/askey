#!/bin/sh

cd /mnt/.data/upd

instlr="`find ./ -name '*.run'`"

if [ -n "$instlr"  ]; then

    echo ">>> *.run file exist (download from server) <<<"

    mv $instlr $instlr.exec

        sync

    echo ">>> and .exec <<<"

else

    echo ">>> *.run file not exist (Not download from server) <<<"

    instlr="`find ./ -name '*.installer'`"

    if [ -n "$instlr"  ]; then

        mv $instlr $instlr.NDL

                sync

        echo ">>> and .NDL <<<"

        else

        echo ">>> can't find *.installer !!! <<<"

        fi

fi

/opt/qcom/bin/tests/fsmWebServer &

#/opt/qcom/bin/ptp1588 --transport=udp --logtfcs &

echo Askey_PP_6.7.1_MS5_v18_TDD > /etc/issue
