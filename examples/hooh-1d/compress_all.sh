#!/bin/bash

find -name 'opt_tmp' -execdir tar zcf opt_tmp.tar.gz opt_tmp/ \;
