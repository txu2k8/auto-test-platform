import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/api/user_auth/user/login',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/api/user_auth/user/info',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/api/user_auth/user/logout',
    method: 'post'
  })
}
