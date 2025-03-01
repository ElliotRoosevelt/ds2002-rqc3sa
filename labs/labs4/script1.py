#!/bin/bash

set -e

LOCAL_FILE=$1
BUCKET_NAME=$2
EXPIRATION=$3

aws s3 cp "$LOCAL_FILE" "s3://$BUCKET_NAME/$(basename "$LOCAL_FILE")" --acl private

aws s3 presign "s3://$BUCKET_NAME/$(basename "$LOCAL_FILE")" --expires-in "$EXPIRATION"

