from fir_interpolate_hb import *
from aie_common import *
from vmc_fir_utils import *

#### VMC validators ####
def vmc_validate_coef_type(args):
    data_type = args["data_type"]
    coef_type = args["coef_type"]
    return fn_validate_coef_type(data_type, coef_type)
	

def vmc_validate_input_window_size(args):
	input_window_size = args["input_window_size"]
	data_type = args["data_type"]
	use_coeff_reload = args["use_coeff_reload"]
	coef_type = args["coef_type"]
	coeff = args["coeff"]
	api = 0
	ssr = 1
	if input_window_size < 4:
	    return isError(f"Minimum value for parameter Input window size is 4, but got {input_window_size}.")
	fir_length = fn_get_fir_length_hb(args)
	return deci_hb.fn_validate_input_window_size(data_type, coef_type, fir_length, input_window_size, api, ssr)

def vmc_validate_casc_length(args):
    casc_length = args["casc_length"]
    return fn_validate_casc_len(casc_length);
    

def vmc_validate_coeff(args):
	use_coeff_reload = args["use_coeff_reload"]
	coef_type = args["coef_type"]
	coeff = args["coeff"]
	data_type = args["data_type"]
	casc_length = args["casc_length"]
	ssr = 1
	interp_poly = args["interp_poly"]
	api = 0
	fir_length = fn_get_fir_length_hb(args)
	return fn_validate_fir_len(data_type, coef_type, fir_length, casc_length, ssr, api, use_coeff_reload, interp_poly)

def validate_sat_mode(args):
    sat_mode = args["sat_mode"]
    return fn_validate_satMode(sat_mode);

def vmc_validate_shift_val(args):
	data_type = args["data_type"]
	shift_val = args["shift_val"]
	return fn_validate_shift(data_type, shift_val)
    
def vmc_validate_upshift_ct(args):
	data_type = args["data_type"]
	upshift_ct = args["upshift_ct"]
	AIE_VARIANT = args["AIE_VARIANT"]
	return fn_validate_upshift_ct(data_type, upshift_ct, AIE_VARIANT)

def vmc_validate_interp_poly(args):
        interp_poly = args["interp_poly"]
        ssr = 1
        api = 0
        ret = fn_validate_para_interp_poly(api, interp_poly, ssr)
        if ret["is_valid"] == False:
          err_msg = ret["err_message"]
          err_msg = err_msg.replace("TP_PARA_INTERP_POLY", "'Interpolate polyphase'")
          return {"is_valid": False, "err_message": err_msg}
        else:
          return {"is_valid": True}

def vmc_validate_ssr(args):
    ssr = 1
    api = 0
    return fn_validate_ssr(api,ssr)

def vmc_validate_input_ports(args):
    dual_ip = args["dual_ip"]
    AIE_VARIANT = args["AIE_VARIANT"]
    return fn_validate_num_inputs(dual_ip, AIE_VARIANT)

def vmc_validate_interpolate_factor(args):
	interpolate_factor = args["interpolate_factor"]
	return fn_validate_interpolate_factor(interpolate_factor)

def vmc_validate_out_ports(args):
	num_outputs = fn_get_num_outputs(args)
	interp_poly = args["interp_poly"]
	dual_ip = args["dual_ip"]
	AIE_VARIANT = args["AIE_VARIANT"]
	return fn_validate_num_outputs(interp_poly, dual_ip, num_outputs, AIE_VARIANT)

def vmc_validate_rnd_mode(args):
	rnd_mode = args["rnd_mode"]
	AIE_VARIANT = args["AIE_VARIANT"]
	return fn_validate_roundMode(rnd_mode, AIE_VARIANT)

#### VMC graph generator ####
def vmc_generate_graph(name, args):
    tmpargs = {}
    tmpargs["TT_DATA"] = args["data_type"]
    tmpargs["TT_COEF"] = args["coef_type"]
    tmpargs["TP_FIR_LEN"] = fn_get_fir_length_hb(args)
    tmpargs["TP_SHIFT"] = args["shift_val"]
    tmpargs["TP_RND"] = args["rnd_mode"]
    tmpargs["TP_INPUT_WINDOW_VSIZE"] = args["input_window_size"]
    tmpargs["TP_CASC_LEN"] = args["casc_length"]
    tmpargs["TP_USE_COEF_RELOAD"] = 1 if args["use_coeff_reload"] else 0
    tmpargs["TP_NUM_OUTPUTS"] = fn_get_num_outputs(args)
    tmpargs["TP_DUAL_IP"] = 1 if args["dual_ip"] else 0
    tmpargs["TP_API"] = 0
    tmpargs["TP_SSR"] = 1
    tmpargs["coeff"] = args["coeff"]
    tmpargs["TP_UPSHIFT_CT"] = args["upshift_ct"]
    tmpargs["TP_PARA_INTERP_POLY"] = args["interp_poly"]
    tmpargs["TP_SAT"] = args["sat_mode"]
   
    return generate_graph(name, tmpargs)
