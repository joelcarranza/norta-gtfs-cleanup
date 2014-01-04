set -e
TARGET=gtfs-out

if [ -z "$1" ]
  then
    echo "Must supply input file"
    exit -1
fi

INFILE=$1
OUTFILE=${1%.zip}.clean.zip
rm -rf $TARGET
unzip -o $INFILE -d $TARGET

python update_route_codes.py $TARGET
python clean_trip_names.py $TARGET
python clean_stop_names.py $TARGET
python amend_bikes_allowed.py $TARGET

zip -j "$OUTFILE" $TARGET/*.txt

echo "Wrote $OUTFILE"
