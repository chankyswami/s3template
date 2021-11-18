#!/bin/bash
echo -n "Enter the name of target AWS account: "
read;
ACCOUNT=${REPLY}
unset REPLY
echo You typed ${ACCOUNT}}
echo -n "Enter the name of bucket: "
read;
BUCKET_NAME=${REPLY}
unset REPLY
echo You typed ${BUCKET_NAME}
echo -n "Enable versioning or not ? Valid entries are True or False: "
read;
VERSIONING=${REPLY}
unset REPLY
echo You typed ${VERSIONING}
echo -n "Enter owner of bucket: "
read;
OWNER=${REPLY}
unset REPLY
echo You typed ${OWNER}
echo -n "Enter project which holds bucket: "
read;
PROJECT=${REPLY}
unset REPLY
echo You typed ${PROJECT}
echo "Provisioning resources in: " $ACCOUNT
cdk deploy -c bucket_name=$BUCKET_NAME -c versioning=$VERSIONING -c tag_owner=$OWNER -c tag_project=$PROJECT --profile $ACCOUNT
