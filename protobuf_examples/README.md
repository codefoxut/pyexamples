I am following a course by 

> You cannot use the numbers 19000 through 19999 because google has reserved them.

>* Tags numbered from 1 to 15 use 1 byte in space, so use them from frequently populated fields.
>* Tags numbered from 2 to 2047 use 2 bytes.


> *js -> protoc -I=protobuf_examples --js_out=protobuf_examples/jsprotos  PROTO_FILES
> *java -> protoc -I. --java_out=protobuf_examples/jprotos  PROTO_FILES
> *python -> protoc -I. --python_out=protobuf_examples/jprotos  PROTO_FILES
