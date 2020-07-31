./maestro --print_res=true \
          --print_res_csv_file=false \
          --print_log_file=false \
          --Mapping_file='data/mapping/Resnet50_kcp_ws.m' \
          --HW_file='./data/hw/accelerator_1.m' \
          --noc_bw=32 \
          --noc_hops=1 \
          --noc_hop_latency=1 \
          --l1_size=256 \
          --l2_size=2048 \
          --num_pes=256 \
          --print_design_space=true \
          --msg_print_lv=2

