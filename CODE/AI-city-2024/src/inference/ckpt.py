import sys
sys.path.append('../utils')
from utils import save_json

ckpt = {
    'external':{
        'pedes':{
            'appearance': 'trinhxuankhai/external_pedes_appearance',
            'environment': 'trinhxuankhai/external_pedes_environment',
            'location': 'trinhxuankhai/external_pedes_location',
            'attention': 'trinhxuankhai/external_pedes_attention',
            'rewrite': 'trinhxuankhai/external_pedes_rewrite',
        },
        'vehicle':{
            'appearance': 'trinhxuankhai/external_vehicle_appearance',
            'environment': 'trinhxuankhai/external_vehicle_environment',
            'location': 'trinhxuankhai/external_vehicle_location',
            'action': 'trinhxuankhai/external_vehicle_action',
            'rewrite': 'trinhxuankhai/external_vehicle_rewrite',
        }
    },
    'internal':{
        'overhead_view':{
            'pedes':{
                'appearance': 'trinhxuankhai/origin_o_pedes_appearance',
                'environment': 'trinhxuankhai/origin_o_pedes_environment',
                'location': 'trinhxuankhai/origin_o_pedes_location',
                'attention': 'trinhxuankhai/origin_o_pedes_attention',
                'rewrite': 'trinhxuankhai/origin_o_pedes_rewrite',
            },
            'vehicle':{
                'appearance': 'trinhxuankhai/origin_o_vehicle_appearance',
                'environment': 'trinhxuankhai/origin_o_vehicle_environment',
                'location': 'trinhxuankhai/origin_o_vehicle_location',
                'action': 'trinhxuankhai/origin_o_vehicle_action',
                'rewrite': 'trinhxuankhai/origin_o_vehicle_rewrite',
            },
        },
        'vehicle_view':{
            'pedes':{
                'appearance': 'trinhxuankhai/origin_v_pedes_appearance',
                'environment': 'trinhxuankhai/origin_v_pedes_environment',
                'location': 'trinhxuankhai/origin_v_pedes_location',
                'attention': 'trinhxuankhai/origin_v_pedes_attention',
                'rewrite': 'trinhxuankhai/origin_v_pedes_rewrite',
            },
            'vehicle':{
                'appearance': 'trinhxuankhai/origin_v_vehicle_appearance',
                'environment': 'trinhxuankhai/origin_v_vehicle_environment',
                'location': 'trinhxuankhai/origin_v_vehicle_location',
                'action': 'trinhxuankhai/origin_v_vehicle_action',
                'rewrite': 'trinhxuankhai/origin_v_vehicle_rewrite',
            },
        }
    }
}

save_json('ckpt.json', ckpt)