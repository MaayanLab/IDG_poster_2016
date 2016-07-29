
/*
Example files
*/
// make_clust('hgram_4_fam_no_cats.json');
make_clust('hgram_4_fam_with_cats.json');

function make_clust(inst_network){

    d3.json('json/'+inst_network, function(network_data){

      // define arguments object
      var args = {
        root: '#container-id-1',
        'network_data': network_data,
        'about':'Zoom, scroll, and click buttons to interact with the clustergram.',
        'row_tip_callback':gene_info,
        'tile_colors': ['#000000', '#1C86EE']
      };

      resize_container(args);

      d3.select(window).on('resize',function(){
        resize_container(args);
        cgm.resize_viz();
      });

      cgm = Clustergrammer(args);

      d3.select(cgm.params.root + ' .wait_message').remove();

      // // temporarily disabling enrichr categories
      // ////////////////////////////////////////////
      // enr_obj = Enrichr_request(cgm);
      // enr_obj.enrichr_icon();

  });

}

function resize_container(args){

  var screen_width = window.innerWidth;
  var screen_height = window.innerHeight - 20;

  d3.select(args.root)
    .style('width', screen_width+'px')
    .style('height', screen_height+'px');
}
