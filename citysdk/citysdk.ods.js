CitySDK.prototype.modules.ods = new ODSModule();

function ODSModule() {
    this.enabled = false;
};

ODSModule.prototype.enable = function () {
    this.enabled = true;
};

swagger = new SwaggerClient({
    url: "http://public.opendatasoft.com/api/v2/swagger.json",
    success: function () {
        Object.getOwnPropertyNames(swagger.default.operations).forEach(function (method_name) {
            ODSModule.prototype[method_name] = function (request, callback, callbackerror) {
                swagger.default[method_name](
                    request,
                    function (response) {
                        callback(response.obj);
                    },
                    function (response) {
                        callbackerror(response);
                    });
            }
        });
    }
});

/*
 get: module.exports
 get_source: module.exports
 get_source_datasets: module.exports
 get_source_datasets_dataset_id: module.exports
 get_source_datasets_dataset_id_attachments: module.exports
 get_source_datasets_dataset_id_attachments_attachment_id: module.exports
 get_source_datasets_dataset_id_files: module.exports
 get_source_datasets_dataset_id_files_file_id: module.exports
 get_source_datasets_dataset_id_records: module.exports
 get_source_datasets_dataset_id_records_record_id: module.exports
 get_source_datasets_dataset_id_reuses: module.exports
 get_source_datasets_dataset_id_reuses_reuse_id: module.exports
 get_source_datasets_dataset_id_snapshots: module.exports
 get_source_datasets_dataset_id_snapshots_snapshot_id: module.exports
 get_source_metadata_templates: module.exports
 get_source_metadata_templates_metadata_template_type: module.exports
 get_source_metadata_templates_metadata_template_type_metadata_template_name: module.exports
 post_source_aggregates: module.exports
 post_source_datasets_dataset_id_aggregates: module.exports
 put_source_datasets_dataset_id_feedback: module.exports
 */
